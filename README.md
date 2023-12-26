# avanti-devops-challenge


1. Criar o Dockerfile da App ✅ <br>
1.1 Instalar os requisitos para a app funcionar (requirements.txt) ✅

2. Criar um cluster k8s com 2 nós<br>
2.1 2 Nós<br>
2.2 Instalar algum tipo de dashboard (rancher, k8s dashboard, etc)<br>

3. Criar os manifestos do Kubernetes<br>
3.1. Prever ambiente de Dev e Prod (kustomize)<br>
3.2. Deployment(executar a cada 1 minuto) para gerar mensagens na fila<br>
3.3. Parâmetros:<br>
3.3.1. Nome (configMap)<br>
3.3.2. Timer (configMap)<br>
3.3.3. Mensagem (secret)<br>
3.3.4. URL (secret)<br>

4. Pipeline<br>
4.1. CI (Github Actions)<br>
4.1.1. Checar segurança do código (bandit)<br>
4.1.2. Checar qualidade do código (pyLint)<br>
4.1.3. Rodar testes unitários (pyTest)<br>
4.2. CD  (Github Actions / ArgoCD)<br>
4.2.1. Gerar a imagem da aplicação (docker hub - imagem pública)<br>
4.2.2. Deploy no K8S<br>

5. Monitoramento (Prometheus / Grafana / AlertManager)<br>
5.1. Saúde da aplicação<br>
5.2. Saúde do RabbitMQ<br>




