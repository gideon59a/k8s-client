'''
Per: https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/
example from: https://github.com/kubernetes-client/python/blob/master/examples/example1.py
'''

from kubernetes import client, config

def _k8s_client(config):
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    try: k*
        if not conf.kubernetes.config_file:
            print ('kubernetes config file is not defined')
            return

        kubeconf = conf.kubernetes.config_file
        print (kubeconf)

        config.load_kube_config(config_file=kubeconf)
        # or:    config.load_kube_config()

        k8s_client = client.CoreV1Api()

        if k8s_client is None:
            print ('k8s client returns None')
            return

        return k8s_client

    except Exception:
        print ('try failed. Create k8s client - Got Exception')


def main():
    print ("k8s client")
    k8s_client = _k8s_client(config)




def refmain():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()


#############REF
def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    config.load

    config.load_kube_config("kubeconfig") # kubeconfig is the local config file name

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
