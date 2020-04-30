# ansible full ELK in one script

## Cofigure
check & set hosts inside [main inventory](inventory)

## Contents
- [main](main.yml)
- [prepare hosts (setup docker / pip)](init-hosts.yml)
- [elasticsearch setup](elasticsearch.yml)
- [kibana setup](kibana.yml)
- [logstash setup](logstash.yml)

## Run
```bash
ansible-playbook -i inventory main.yml
```

## Enjoy