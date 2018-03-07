---
layout: default
title: collection interface
pdf: true
permalink: /interface
toc: false
---

# Interfaces

### Teams
Singularity Registry allows registry staff (and if the administrators allow it) authenticated users to create teams, or groups of users that want to colleaborate on container collections together.

![teams.png](assets/img/teams.png)

If you are allowed to create and manage teams (see the setup page section about [teams](/sregistry/setup#teams) for information about this) the team permission level determines how others are added to the team.  If a team is **open**, then anyone can join. If it's **invite** only, then you need to generate an invitation. To do this, you can navigate to your Team page, and click the button to "Invite User":

![team-invite.png](assets/img/team-invite.png)

The interface will give you a link to send to your colleague to join him or her to the team. Once used, it will expire.

![team-invite-link.png](assets/img/team-invite-link.png)

Membership in teams is important because when you add another user as a collaborator to one of your collections (either an owner ot member) they must be part of one of your teams.


### Collections 
The most important control panel for your collections is the Settings page. You can access it via the "Settings" button at the top of the collection view. The most likely action you will want to do is add other users from your teams (as described above). You do this on each Collection settings page:

![team-settings.png](assets/img/team-settings.png)

For example, if my lab has a set of users on sregistry and we intend to build images together, we would make a team for our lab, and then easily find one another to manage access to images.



## Badges
Recently added, you can get a badge to link to your collection

![assets/img/badges.png](assets/img/badges.png)

### Users
You might want to give other users control of your collection (to push and pull and generally manage), and these are called **owners**. You might also want to give some users pull access, most relevant if your collection is private. You can do that in the "Contributors" tab of the settings page:

![assets/img/team-settings.png](assets/img/team-settings.png)

Remember that you can only choose to add individuals that are part of one of your teams. This means that you should generally make a team first.

### Danger Zone
And of course if you need to delete, the settings page has a Danger Zone. Be careful!

![assets/img/danger.png](assets/img/danger.png)

<div>
    <a href="/sregistry/setup"><button class="previous-button btn btn-primary"><i class="fa fa-chevron-left"></i> </button></a>
    <a href="/sregistry/client"><button class="next-button btn btn-primary"><i class="fa fa-chevron-right"></i> </button></a>
</div><br>
