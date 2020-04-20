## Synopsis
-mailsend neuron for Kalliope 0.5<0.6
## require
- python 3 or python 2.7
- kalliope core installed

## Installation
```bash
cd (your kalliope)
kalliope install --git-url https://github.com/satt105/mailsend.git
```

## Options

| Parameter   | Required | Choices                          |description |
|-------------|----------|---------------------------------|---------------------------------|
| Fromadd     | yes      | string                          |the sender's address             |
| MDP         | yes      | string                          |it is recommended to hide passwords in variables rather than data in each synapse|
| Toadd       | yes      | string                          |the recipient's email address    |
| message     | yes      | string                          |the content of the mail          |
## Notes
- The module is a beta version under development, it is possible that the production of errors
- The module is developed by the community for the kalliope project. It can be modified and updated
- you had to go to your google account is allowed https://myaccount.google.com/security and allowed "Less secure application access"
## Synapses example configuration
```
  - name: "test-send"
    signals:
      - order: "Send Mark that I'm anonymous."
    neurons:
      - mailsend:
          Fromadd: "supersecret@gmail.com"
          MDP: "{{thepassword}}
          Toadd: "thismy@gmail.com"
          message: "Hello, I'm anonymous."

  - name: "test-send"
    signals:
      - order: "Send Mark {{ message }}"
    neurons:
      - mailsend:
          Fromadd: "supersecret@gmail.com"
          MDP: "{{thepassword}}
          Toadd: "thismy@gmail.com"
          message: "{{ message }}"
```




