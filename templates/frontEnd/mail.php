<?php
    $username = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['phone'];
    $message = $_POST['message'];
    $submit = $_POST['submit'];

    // reciever mail address
    $to = 'tfthemecafe@gmail.com';
    $subject = 'Mail From Loan Plus HTML Template.';
    $headers = 'From: ' . $email . "\r\n" . 'Reply-To: ' . $to . "\r\n";
    if(isset($submit)){
        if( !empty($username) && !empty($email) && !empty($message) ){
            mail($to, $subject, $message, $headers);
            header('Location: thank-you.html');
        }
    }
?>