
# Docker tasks




## 1. Membuat Image dari Github Repository
- Buat file dengan command `vim Dockerfile`
```Dockerfile
FROM python:3.8
WORKDIR /app
COPY . /app
EXPOSE 8081
CMD ["python", "todo.py"]
```
- build docker dengan command `docker build -t todo-app`

## 2. Menjalankan image tersebut sebagai container dan berjalan pada port 8081

Untuk menjalankan image bisa gunakan command `docker run -it --expose 8081 todo-app`
## 3. Mencari IP Docker container 'whoami'
menggunakan inspect :
- Untuk mencari bisa menggunakan command `docker inspect whoami`
- lalu cari yang menampilkan bagian ip address
- hasilnya `IP address : 172.17.0.2`

alternatif lain :
- hanya menampilkan output ip address `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whoami`




## 4. Apa isi dari file yang tersembunyi dari docker container 'whoami'? clue volume mounting

- inspect menggunakan `docker inspect whoami`
- cari bagian Mounts > Source
```
"Mounts": [
            {
                "Type": "bind",
                "Source": "/home/local/.docker",
                "Destination": "/tmp/system",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
```
- ubah direktori ke `"/home/local/.docker"`
- jalankan `ls` untuk menampilkan isi folder
- terdapat file `whoami`, untuk melihat isinya bisa menggunakan `cat whoami`
- hasilnya `"Oofooni1eeb9aengol3feekiph6fieve"`
## 5. image apa yang digunakan pada docker contaienr 'whoami'
menggunakan inspect :
- Untuk mencari bisa menggunakan command `docker inspect whoami`
- lalu cari yang pada bagian config > image

alternatif lain :
- hanya menampilkan output nama image langsung
`docker inspect -f '{{ .Config.Image }}' whoami`

hasil pencarian image yang digunakan adalah : 
`"secret:aequaix9De6dii1ay4HeeWai2obie6Ei"`