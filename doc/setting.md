# Setting

## global configuration

### data_file

`data_file` is the path of the yaml dataset.

Exemple of **my_dataset.yaml**:
```
my_url_to_chek: hash_value
```

### algorithm
`algorithm`: the hash algorithm used to check the integrity of the web page
You can choose :
- `sha1`
- `sha256`
- `md5`
- `all` for all hash algorithm.

### send_alert_if_check

`send_alert_if_check`: is the field in wich you chose to alert or not
You can choose:
- `all` to alert when integrity is good or not
- `false` to alert if the check failed


### Exemple of global configuration
```yaml
# ============================ Configuration =============================
# -- data --
data_file: my_dataset.yaml

# -- hash algorithm --
algorithm: md5

# -- conditions of alerting --
# choic is 'all', true of false
send_alert_if_check: false
```

## Alerter

The alerter section is defined with `alerter` dict.

- `scheme`: scheme to use, "https" or "https"
- `url`: url to send the alert
- `method`: the method to be used for sending the request, the choice is "POST", "PUT" or "PATCH"

### Basic Authentification

If you want to use an authentification with user and password
`basic_auth`:
  - `user`: user name
  - `password`: password

### Token Authentification

If you want to use an token authentification use this:
`token`: your toekn

### header

You can set custome header as dict with yaml syntax
`header`: your header

Exemple:
```yaml
header:
  Content-Type: application/json
```

### SSL cert
- `ssl`: the path of your ca certificate
- `verify_ssl`: If you do not want to check the SSL certificate, set this to false

### Exemple of alerter configuration
```yaml
# ================================ Alerter ================================
alerter:
  scheme: "https"
  url: my_rul
  # choice is POST, PUT or PATCH
  method: POST

  # -- Basic Authentification --
  # basic_auth:
  #   user: my_user
  #   password: my_password

  # -- token Authentification --
  # token: my_token

  # -- header --
  # header:
  # -- using ssl --
  # ssl: my_ca
  # -- diabsle ssl verify --
  ssl_verify: false
```

## Template

The template section is defined with `template` dict.

`data`: content of the template, support the **jinja syntax**

### Data

You can inject this fielads in your message template:
- `url`: the url to check
- `original_hash`: the hash store in dataset file
- `actual_hash`: the actually hash of the url
- `algorithm`: the hash algorithm used
- `http_check_status_code`: status code of the http request
- `check`: the resut of the integrity check

### Exemple of template:
```yaml
# =============================== Template ================================
template:
  data: |
    Integrity check verification failed for url: {{ url }}
    - original hash {{ original_hash }}
    - hash found {{ actual_hash }}
    - hash algorithm: {{ algorithm }}

    status_code for url requesting: {{ http_check_status_code }}
```

## Exemple of configuration file:

```yaml
# ============================ Configuration =============================
# -- data --
data_file: my_dataset.yaml

# -- hash algorithm --
algorithm: md5

# -- conditions of alerting --
# choic is 'all', true of false
send_alert_if_check: false

# ================================ Alerter ================================
alerter:
  scheme: "https"
  url: my_rul
  # choic is POST, PUT or PATCH
  method: POST

  # -- Basic Authentification --
  # basic_auth:
  #   user: my_user
  #   password: my_password

  # -- token Authentification --
  # token: my_token

  # -- header --
  # header:
  # -- using ssl --
  # ssl: my_ca
  # -- diabsle ssl verify --
  ssl_verify: false
# =============================== Template ================================
template:
  data: |
    Integrity check verification failed for url: {{ url }}
    - original hash {{ original_hash }}
    - hash found {{ actual_hash }}
    - hash algorithm: {{ algorithm }}

    status_code for url requesting: {{ http_check_status_code }}
```