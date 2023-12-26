# avanti-devops-challenge


✅ 1. Criar o Dockerfile da App  <br>
✅ 1.1 Instalar os requisitos para a app funcionar (requirements.txt) 

✅ 2. Criar um cluster k8s com 2 nós<br>
✅ 2.1 2 Nós<br>
✅ 2.2 Instalar algum tipo de dashboard (rancher, k8s dashboard, etc)<br>

✅ 3. Criar os manifestos do Kubernetes<br>
✅ 3.1. Prever ambiente de Dev e Prod (kustomize)<br>
❌ 3.2. Deployment(executar a cada 1 minuto) para gerar mensagens na fila<br>
❌ 3.3. Parâmetros:<br> 
❌ 3.3.1. Nome (configMap)<br> 
❌ 3.3.2. Timer (configMap)<br> 
❌ 3.3.3. Mensagem (secret)<br> 
❌ 3.3.4. URL (secret)<br> 

✅ 4. Pipeline<br>
✅ 4.1. CI (Github Actions)<br>
✅ 4.1.1. Checar segurança do código (bandit)<br>
✅ 4.1.2. Checar qualidade do código (pyLint)<br>
✅ 4.1.3. Rodar testes unitários (pyTest)<br>
✅ 4.2. CD  (Github Actions / ArgoCD)<br>
✅ 4.2.1. Gerar a imagem da aplicação (docker hub - imagem pública)<br>
✅ 4.2.2. Deploy no K8S<br>

5. Monitoramento (Prometheus / Grafana / AlertManager)<br>
5.1. Saúde da aplicação<br>
5.2. Saúde do RabbitMQ<br>





----------------------------

1. pedir a instalação do homebrew
2. para rodar o _project-final.yaml tem criar um cluster 
para isso tem que instalar o k3d e rodar o comando k3d cluster create nome-cluster

- execute esse comando para dar inicio ao dashboard "kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml"

execute o service "kubernetes-dashboard.yaml"

use o comando "kubectl -n kubernetes-dashboard create token admin-user" para obter
a chave de acesso do dashboard


e execute o comando "kubectl proxy" executar o dashboard 

no endereço "http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login"

cole o token





kustomizer: fazer a descrição pela instalado do homebrew 
- comando para gerar os yaml 

    - kubectl apply -k base
    - kubectl apply -k overlays/dev
    - kubectl apply -k overlays/prod




pipelines
 - instalar o act via homebrew



para usar o argocd

- kubectl create namespace argocd
- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
- kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

- rode o comando "kubectl -n argocd get po,svc" procurr o service/argocd-repo-server
- execute o comando com o nome do service/argocd-server "kubectl -n argocd port-forward service/argocd-server 8080:443"

acesse o endereço localhost:8080 por padrão o user vem como "admin"
- abra um novo terminal rode o comando "argocd admin initial-password -n argocd" para exibir a senha no terminal, esse comando so vai funcionar se o [argocd cli](https://argo-cd.readthedocs.io/en/stable/cli_installation/) estiver instalado 

- clique em "new app"
- em Application Name ponha o nome do projeto "Avanti"
- em Project Name ponha default
- na SOURCE ponha o endereço do repositorio "https://github.com/luisc05ta/avanti-devops-challenge.git"
- Em revision escolha o "kustomize/base"
- na aba DESTINATION coloque no "Cluster URL" o endereço sugerido pela ferramenta e o Namespace coloque "default"
- por fim aperte em "Create"

![ArgoCD](.images/argocd.png)


<br>
minhas imagens 
- https://hub.docker.com/repository/docker/lu15c05ta/write/general
- https://hub.docker.com/repository/docker/lu15c05ta/read/general

caso queira deletar as senhas e os services de do dashboart: => <br />
"kubectl -n kubernetes-dashboard delete serviceaccount admin-user"<br />
"kubectl -n kubernetes-dashboard delete clusterrolebinding admin-user"




