import os
from kubernetes import client, config

'''configuration = client.Configuration()
api_client = client.ApiClient(configuration)
v1 = client.CoreV1Api(api_client)
ret = v1.list_namespaced_pod(namespace="paas-content-storefront-18", watch=False)
for pod in ret.items:
    print(f"Name: {pod.metadata.name}, Namespace: {pod.metadata.namespace} IP: {pod.status.pod_ip}")'''

'''pod = os.system ('kubectl -n  paas-content-storefront-18 get pods -o custom-columns=":metadata.name"| grep app-stf-sbermarket')
print('pod is %d' % pod)
print(pod)
os.system('kubectl exec -n paas-content-storefront-18 -it app-stf-sbermarket-597bfffc95-4nlj8 -c app-puma --  /paas-entrypoint/entrypoint rails c')'''

config.load_kube_config()
api = client.AppsV1Api()

deployments = api.list_namespaced_deployment(namespace="paas-content-storefront-18")
for deployment in deployments.items:
    print(deployment.metadata.name)
pod = v1.list_pod_for_all_