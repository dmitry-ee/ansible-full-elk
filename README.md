# ansible full ELK

## Cofigure
check & set hosts inside [main inventory](inventory)

## Contents
- [main](main.yml)
- [prepare hosts (setup docker / pip)](init-hosts.yml)
- [elasticsearch setup](es.yml)
- [kibana setup](kibana.yml)
- [logstash setup](logstash.yml)
- [use logstash script](logstash.yml#L39)

## Run
```bash
ansible-playbook -i inventory main.yml
```

## Enjoy