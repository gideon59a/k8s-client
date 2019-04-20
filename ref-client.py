# https://github.com/kubernetes-client/python/blob/master/examples/example1.py

# The following k8s client accesses the k8s cluster kubectl proxy that runs on http port 8888
# (the proxy was created by: # kubectl proxy --address='0.0.0.0' -p 8888 --accept-hosts='.*' &  )
# the 'kubeconfig" file below was copied from the real cluster and put in this py files folder.
# As I used http access to the proxy, no tls keys/certs were needed for the client.

from kubernetes import client, config

def main():
    # Configs can be setad in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    config.load_kube_config("kubeconfig") # kubeconfig is the local config file name

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
