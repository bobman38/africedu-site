Title: Contact
Date: 2008-07-26 12:41
Author: admin
Slug: contact
pageorder: 30

<form action="//formspree.io/contact@africedu.fr" method="POST">
  <div class="form-group">
    <label for="name">Nom</label>
    <input type="text" class="form-control span8" id="name" aria-describedby="nameHelp" placeholder="Entrer nom" required>
  </div>
  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" class="form-control span8" id="email" placeholder="Email" required>
  </div>
  <div class="form-group">
    <label for="message">Message</label>
    <textarea class="form-control span8" id="message" name="message" rows="7" required></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Envoyez</button>
  <input type="hidden" name="_language" value="fr" />
  <input type="hidden" name="_next" value="/pages/thanks.html" />
  <input type="hidden" name="_subject" value="Message du site africedu.fr">
</form>