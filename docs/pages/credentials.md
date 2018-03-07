---
layout: default
title: Credentials
pdf: true
permalink: /credentials
toc: false
---

# Accounts

### User Accounts
If you remember from the [setup](/sregistry/setup#create-accounts) you created your first superuser account by giving permission to your account from the command line inside the container. For doing this again, you don't need to interact with the container in this way, but instead, you can manage admins (and other superusers) from the web interface. When logged in to your superuser account, you will see an "Admin" link in your profile in the top right:

![admin-option.png](assets/img/admin-option.png)

This will take you to the administrative panel. Once there, you can click on "Users" at the bottom of the list, and then see a list of users to edit, with filters in the right panel.

![admin-users.png](assets/img/admin-users.png)

Once you select a user, there will be checkboxes to give staff or superuser status, along with other options.


### Secrets
After you create a user, you will need a way to communicate to the registry, and validate your identity. We need to put our credentials in a hidden file called `.sregistry` in our `$HOME` directory. Each time we use the client, the secrets is used to encrypt a call and time-specific token that the registry can un-encrypt with the same key, and verify the payload. After creating your account in [setup](/sregistry/setup), making yourself a superuser and admin and logging in (remember this part?)


```
NAME=$(docker ps -aqf "name=sregistry_uwsgi_1")
docker exec $NAME python /code/manage.py add_superuser --username vsoch
docker exec $NAME python /code/manage.py add_admin --username vsoch
```

You will want to go to [http://127.0.0.1/token](http://127.0.0.1/token) and copy paste the entire json object into a file called `.sregistry` in your `$HOME` folder. **Important** you must be a superuser **and** admin to build images. If you don't add yourself as an admin, the menu looks like this:

![/assets/img/without-superuser.png](assets/img/without-superuser.png)

As an admin, you see the button for "token":

![/assets/img/with-superuser.png](assets/img/with-superuser.png)


Here is the token page - note the button on the left will copy the text to your clipboard, for pasting in a file at `$HOME/sregistry`.

![/assets/img/token.png](assets/img/token.png)

Now when we try to communicate with [the client](/sregistry-cli/client-registry), it finds the token and can identify us. 

```
export SREGISTRY_CLIENT=registry
sregistry list
No container collections found.
```

Next, see if you are interested in activating any additional [plugins](/sregistry/plugins) for your Singularity Registry.

<div>
    <a href="/sregistry/setup"><button class="previous-button btn btn-primary"><i class="fa fa-chevron-left"></i> </button></a>
    <a href="/sregistry/plugins"><button class="next-button btn btn-primary"><i class="fa fa-chevron-right"></i> </button></a>
</div><br>
