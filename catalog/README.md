# Item Catalogue

Part of Udacity's Full Stack Web Developer Nanodegree

This project creates a RESTful web application using the Python framework Flask that provides a list of items within a variety of categories and integrates third-party OAuth user registration and authentication as well. Only authenticated users will be able to make changes to the database by implementing CRUD (create, read, upadate an delete) operations using SQLAlchemy. This application also provides a JSON endpoint.

## How to Run?

### Requirements:
* [Python 2.7](https://www.python.org/downloads/release/python-2714/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Getting Started:

First, login to your pre-configured Vagrant VM:
```bash
$ vagrant up
$ vagrant ssh
```

Run your application within the VM
```bash
$ cd /vagrant/catalog
$ python application.py
```

Access you application by visiting following URL:
```
http://localhost:8000
```
