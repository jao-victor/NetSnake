DEBIAN 12
GRAYLOG 7
MONGO DB ENTRE 7 E 8
OPEN SEARCH ENTRE 1.1.X 2.19.4



no graylog 4 e 5
 Graylog → OpenSearch externo

Agora (Graylog 6/7 com datanode):

    Graylog Server → Graylog DataNode → OpenSearch interno



    sudo apt-mark hold mongodb-org


no arquivo do mongo eu deixei assim mesmo pq tá tudo local
    net:
  port: 27017
  bindIp: 127.0.0.1

datanode
    openssl rand -hex 32
    passowrd secret: 817a77b765e36f9c7481f5c216878717d3eac4dbb3bcbf236b0e7187b140c2b0

password-sha: c0b2041e7b479a4909650d46dc3685ba42556cfc5bfdd098eb42bde191bff114


Initial configuration is accessible at 0.0.0.0:9000, with username 'admin' and password 'vPwpZzKvmX'.
Try clicking on http://admin:vPwpZzKvmX@0.0.0.0:9000



instalei junto o graylog e o openseac (https://go2docs.graylog.org/current/downloading_and_installing_graylog/operating_system_packages.htm#DEBOperatingSystemPackageInstallation)

e depois instalei o mongodb separado (https://go2docs.graylog.org/current/downloading_and_installing_graylog/debian_installation.htm#InstallMongoDB)

    e segui as configurações dos paramentros