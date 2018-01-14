#!/opt/app/anaconda2/python27/bin

'''
###############################
author: Grant Zukel
copyright: Copyright 2017, ATT&T\
credits: Grant Zukel
license: MIT
version: 1.0.0
maintainer: Grant Zukel
email: gz1139@att.com
status: Production"
description: This is the report script for seed templates. This script needs one file called urls and in this file the user will specify the url endpoints his service uses.

example urls
/apschelp
/sentiment
hc=/apschelp
hcn=http.

hc: is the endpoint the service will look for to ensure its up.
hcn: is the name of the port in the service yaml which your service runs on. This is generally http.
###############################
'''
import os
import smtplib
import subprocess
import sys
import time
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests, base64


def run_command(command):
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        if err:
            output = output + str(err)
        return output
    except Exception as e:
        print "There seems to be an issue running the command: ", command
        return e


def get_pod_logs(name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name, cluster_url):
    print "Checking Deployment Status."
    print "Finding the port for your deployment: ", name
    try:
        while True:
            namespace = namespace.replace(".", "-")
            pod = kubectl + " get pods --namespace " + namespace + " --context " + context + " " + kubeoptions + " | grep " + name + " | awk '{print $1}'"
            pod_output = run_command(pod.strip()).strip()
            pod_command = kubectl + " logs " + pod_output + " -c " + name + " --namespace " + namespace + " --context " + context + " " + kubeoptions
            pod_logs = run_command(pod_command)
            if pod_logs:
                return str(pod_logs)
            else:
                print "Waiting for logs"
                time.sleep(30)
    except Exception as e:
        print e


def service_check(name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name, cluster_url):
    print "Checking Deployment Status."
    print "Finding the port for your deployment: ", name
    try:
        namespace = namespace.replace(".", "-")

        pod = kubectl + " get pods --namespace " + namespace + " --context " + context + " " \
              + kubeoptions + " | grep " + name + " | awk '{print $1}'"
        pod_output = run_command(pod.strip()).strip()

        config_manager_port = kubectl + " describe svc -l app=" + name + " --namespace " + \
                              namespace + " --context " + context + " " + kubeoptions + \
                              " | grep NodePort | sed -E 's/NodePort: +//' | grep " + endpoint_name.strip() + \
                              " | sed -n 's/^.*" + endpoint_name.strip() + "/ /p' | sed -n 's/\/TCP/ /p'"
        port = run_command(config_manager_port)
        endpoint_port = port.strip()
        cluster_url = cluster_url.replace(":", " ")
        cluster_url = cluster_url.replace("http //", "")
        cluster_url_port = cluster_url.split(" ")[1]
        cluster_url = cluster_url.split(" ")[0]

        import socket
        try:
            port_tcp = int(cluster_url_port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((cluster_url, port_tcp))
            if result == 0:
                print "Port is open"
                return 0
            else:
                print "Port is not open"
                return 1
        except:
            return 1
    except Exception as e:
        traceback.print_exc()


def load_test_reports():
    print "Try to load the code scan file."
    try:
        filer_path = os.environ['WORKSPACE'] + "/code_scan"
        filer = open(filer_path, "r").read()
        contents = filer.replace("\n", "<br>")
    except Exception as e:
        error = "The report script had an error: ", str(e)
        traceback.print_exc()
        contents = "Your service didn't appear to have a code scan report in the jenkins workspace name code_scan. Please check your export command."
    return contents


def base_user(username, password):
    usrPass = username + ":" + password
    b64Val = base64.b64encode(usrPass)
    return str(b64Val)


def api_service_check(HOST, health_check, name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name):
    print "Start api service check call on HOST: ", HOST
    print "with the call: ", health_check

    if health_check == "none":
        status_lookup = service_check(name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name, HOST)
        return status_lookup
    elif health_check == "None":
        status_lookup = service_check(name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name, HOST)
        return status_lookup
    elif health_check.lower() == "service":
        status_lookup = service_check(name, kubectl, namespace, context, kubeoptions, endpoint_name, svc_name, HOST)
        return status_lookup
    else:
        try:
            HOST = HOST + health_check

            username = "replace_user"

            password = "replace_password"

            b64val = base_user(username, password)
            headers = {"Authorization": "Basic %s" % b64val}
            r = requests.get(HOST, timeout=10.0, headers=headers)
            print r.status_code
            print r.content

            if r.status_code == 200:
                return 0
            elif r.status_code == 403:
                return 0
            elif r.status_code == 400:
                return 0
            else:
                return 1
        except Exception as e:
            return 1


def check_deployment_status(name, kubectl, namespace, context, kubeoptions, endpoint_name):
    print "Checking Deployment Status."
    print "Finding the port for your deployment: ", name
    status = "None"
    endpoint_port = "None"
    try:
        namespace = namespace.replace(".", "-")
        config_manager_port = kubectl + " describe svc -l app=" + name + " --namespace " + namespace + " --context " \
                              + context + " " + kubeoptions + " | grep NodePort | sed -E 's/NodePort: +//' | grep " \
                              + endpoint_name.strip() + " | sed -n 's/^.*" \
                              + endpoint_name.strip() + "/ /p' | sed -n 's/\/TCP/ /p'"
        port = run_command(config_manager_port)
        endpoint_port = port.strip()
    except Exception as e:
        traceback.print_exc()

    print "Retrieving the deployment status of the pod."
    try:
        kube_command = kubectl + " describe pods " + name + " --namespace " + namespace + " " + kubeoptions
        pods_info = run_command(kube_command)

        for line in pods_info.split("\n"):
            if "Status" in line and "Type" not in line:
                status = line.split()[1].strip()
    except Exception as e:
        traceback.print_exc()

    return endpoint_port, status


def send_email(ingress, direct, status, service_name, user_email, formatted_endpoints):
    print "Build the email report for the user."

    html = """
    <html>
      <head>
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
      </head>
      <style>
      #header-row{
        background-color: #34495E;
        color: #FFF;
      }
      #header-row2{
        background-color: #FFC300;
      }  
      #header-row3{
        background-color: #D6DBDF;
      }    
      </style>
      <body>
            <table class="table" width="100%" cellpadding="5" border="0" cellspacing ="0">
            <tr>
                <td id="header-row"> Service Name </td> <td colspan="2" id="header-row"> """ + service_name + """ </td>
            </tr>
    """

    for endp in formatted_endpoints:
        html += """<tr>
                <td id="header-row"> Ingress </td> <td colspan="2" id="header-row3"> """ + ingress + endp[1:] + """ </td>
            </tr> 
        """

    html += """<tr>
        <td id="header-row"> direct </td> <td colspan="2" id="header-row3"> """ + direct + """ 
        </td>
        </tr><tr><td id="header-row"> test reports </td> <td colspan="2" id="header-row3">  """ + str(
        load_test_reports()) + """ 
        </td>
        </tr>
        """ + status + """

        </table>
    </body>
</html>
    """

    me = user_email
    you = user_email
    service_name = service_name

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Deployment & Testing Report For %s" % service_name
    msg['From'] = me
    msg['To'] = you

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    s = smtplib.SMTP('smtp.it.att.com')
    s.sendmail(me, you, msg.as_string())
    s.quit()


def build_urls():
    try:
        url_file = os.environ['WORKSPACE'] + "/urls"
        url_file = open(url_file, "r").read()
        url_array = url_file.split("\n")
        urls = []
        url_health_check = ""
        url_health_check_type = ""
        svc_name = "None"

        for url in url_array:
            if "hc" in url and "hcn" not in url:
                url_health_check = url.split("=")[1].strip()
            elif "hcn" in url:
                url_health_check_type = url.split("=")[1].strip()
            elif "svc_name" in url:
                svc_name = url.split("=")[1].strip()
            else:
                urls.append(url)

        print("URLS", urls)
        print("URL_HEALTH_CHECK", url_health_check)
        print("URL_HEALTH_CHECK_TYPE", url_health_check_type)

        return urls, url_health_check, url_health_check_type, svc_name
    except:
        traceback.print_exc()
        return [], "", "", ""


def main():
    import timed
    start_time = time.time()
    print("Load environment variables.")

    namespace_ret = os.environ['APP_NS'].replace("-", ".")
    version = os.environ['VERSION']
    HOST = os.environ['K8S_CLUSTER_URL']
    K8S_CONTEXT = os.environ['K8S_CONTEXT']
    K8S_ENVCONTEXT = os.environ['TARGET_ENV']
    K8S_ENVCONTEXT = K8S_ENVCONTEXT.upper()

    K8S_ROUTEOFFER = os.environ['K8S_ROUTEOFFER']
    dockerRegistry = os.environ['dockerRegistry']
    dockerImageRegistry = os.environ['dockerImageRegistry']
    dockerProxyRegistry = os.environ['dockerProxyRegistry']
    K8S_USERNAME = os.environ['K8S_USERNAME']
    K8S_PASSWORD = os.environ.get('K8S_PASSWORD')
    K8S_TOKEN = os.environ.get('K8S_TOKEN')
    K8S_CTX = os.environ['K8S_CTX']
    VERSION = os.environ['VERSION']
    REPLICA_COUNT = os.environ['REPLICA_COUNT']
    SERVICE_ACCOUNT = os.environ['SERVICE_ACCOUNT']
    KUBECTL = os.environ['KUBECTL']
    KUBECTL_OPTS = os.environ['KUBECTL_OPTS']
    APP_NAME = os.environ['APP_NAME']
    NOTIFICATION_EMAIL = os.environ['NOTIFICATION_EMAIL']
    INGRESS_HOST = os.environ['INGRESS_HOST']
    routeOffer = K8S_ROUTEOFFER
    envContext = K8S_ENVCONTEXT
    errors = {}

    urls, urls_health_check, url_health_check_type, svc_name = build_urls()
    print("Starting Service Watcher. This service will tell you when your service is ready.")

    count = 0
    while True:
        try:
            if (K8S_TOKEN != "") and K8S_TOKEN is not None:
                try:
                    KUBECTL_OPTS = "--server=" + HOST +" --insecure-skip-tls-verify=true --token=" + K8S_TOKEN
                except Exception as e:
                    print e 
            elif K8S_PASSWORD is not None:
                try:
                    KUBECTL_OPTS = "--server=" + HOST +" --insecure-skip-tls-verify=true --password=" + K8S_PASSWORD +" --username=" + K8S_USERNAME
                except Exception as k:
                    print k
        except Exception as e:
            print e
            print ("Checking & Waiting for service to be up . . . ")
            endpoint_port, status = check_deployment_status(APP_NAME, KUBECTL, namespace_ret, K8S_CTX, KUBECTL_OPTS,
                                                            url_health_check_type)

            if len(endpoint_port) < 4:
                print "Your service is having issues launching in K8S, please check your KUBECTL Version and your K8S cluster that your service actually deployed."
                if count == 50:
                    sys.exit(2)

            print ("Setting Variables for the check.")
            namespace_ret = namespace_ret.replace("-", ".")
            version = os.environ['VERSION']
            HOST = HOST.replace("https", "http")
            end_point_HOST = str(HOST) + ":" + str(endpoint_port)

            status_api = api_service_check(end_point_HOST, urls_health_check, APP_NAME, KUBECTL, namespace_ret, K8S_CTX,
                                           KUBECTL_OPTS,
                                           url_health_check_type, svc_name)

            print ("Name:", APP_NAME)
            print ("Version: ", version)
            print ("Namespace: ", namespace_ret)
            print ("Endpoint: " + str(HOST) + ":" + str(endpoint_port))
            print (
                "Your service is still pending. Please wait for it to report running. once your service becomes active it will take a few more minutes to register.")

        except Exception as e:
            traceback.print_exc()
            sys.exit(1)

        try:
            if "Running" in status:
                end_point_HOST = str(HOST) + ":" + str(endpoint_port)
                status_api = api_service_check(end_point_HOST, urls_health_check, APP_NAME, KUBECTL, namespace_ret,
                                               K8S_CTX, KUBECTL_OPTS,
                                               url_health_check_type, svc_name)
                print status_api

                if status_api == 0:
                    print("The Microservice API is UP.")
                    break
                else:
                    if count == 200:
                        print("Your service never came up and the max count has been reached.")
                        sys.exit(2)
                    count += 1
                    print("The Microservice isn't responding yet.")
            elif "Pending" in status:
                print("Status is still: Pending")
            elif "Waiting" in status:
                print("Staus is still: Waiting")
            else:
                end_point_HOST = str(HOST) + ":" + str(endpoint_port)
                status_api = api_service_check(end_point_HOST, urls_health_check, APP_NAME, KUBECTL, namespace_ret,
                                               K8S_CTX, KUBECTL_OPTS,
                                               url_health_check_type, svc_name)
                if status_api == 0:
                    print("The Microservice API is UP.")
                    break
                else:
                    if count == 200:
                        print("Your service never came up and the max count has been reached.")
                        sys.exit(2)
                    count += 1
                    print("The Microservice isn't responding yet.")
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)

        time.sleep(60)

    direct = str(HOST) + ":" + str(endpoint_port)

    ingress = INGRESS_HOST + "/service=" + namespace_ret + "." + APP_NAME + "/version=" + VERSION + "/routeOffer=DEFAULT/envContext=" + K8S_ENVCONTEXT + "/subContext=/"

    status_html = "<tr><td colspan='3'> Kubernetes Pod Logs </td> </tr><tr><td colspan='3'>"
    status = get_pod_logs(APP_NAME, KUBECTL, namespace_ret, K8S_CTX, KUBECTL_OPTS, url_health_check_type, svc_name,
                          end_point_HOST)

    for line in status.split("\n"):
        status_html += str(line) + "<br>"
    status_html += "</td></tr>"
    time_taken_in_seconds = (time.time() - start_time)
    time_taken_in_minutes = time_taken_in_seconds / 60.0
    print time_taken_in_minutes

    status_html += "Report script took " + str(time_taken_in_minutes) + " minutes to run."
    # time.sleep(30)
    send_email(ingress, direct, status_html, APP_NAME, NOTIFICATION_EMAIL, urls)


main()

print "The checks have all finished and the report has been sent."

sys.exit(0)
