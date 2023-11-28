# ansible docker container

- buat direktori baru `task-ansible`
- buat file di dalamnya `inventory.yaml`
- buat file juga `playbook.yaml`
- jalanakan ansible dengan `ansible-playbook -i inventory.yaml playbook.yaml`

### jika dibutuhkan upload public key ke vm
- buka terminal windows
- tuliskan command `scp C:\Users\USER\.ssh\id_rsa <user>@btj-academy.bangunindo.io:/home/<user>/.ssh/id_rsa`

### mengubah permision
- `chmod -R 400 /home/<user>/.ssh/id_rsa*`

