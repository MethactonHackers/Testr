<?php
$email = $_POST["email"];
$question = $_POST["question"];
$url = "https://api.sendgrid.com/api/mail.send.json";


$r = new HttpRequest($url, HttpRequest::METH_POST);
$r->setOptions(array('cookies' => array('lang' => 'de')));
$r->addPostFields(array('api_user' => '', 'api_key' => '', 'to' => 'PlanetCookieX@gmail.com', 'toname' => 'PlanetCookieX@gmail.com', 'subject' => 'Question On Testr', 'text' => $question, 'from' => $email));
$r->addPostFile('image', 'profile.jpg', 'image/jpeg');
try {
    echo $r->send()->getBody();
} catch (HttpException $ex) {
    echo $ex;
}

header( 'Location: http://www.yoursite.com/new_page.html' ) ;
?>