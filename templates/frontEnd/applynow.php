<?php
    $lamount = $_POST['lamount'];
    $porpuse_of_loan = $_POST['porpuse_of_loan'];
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $date_of_birth = $_POST['date_of_birth'];
    $martial_state = $_POST['martial_state'];
    $number_of_dependants = $_POST['number_of_dependants'];
    $country = $_POST['country'];
    $city = $_POST['city'];
    $street = $_POST['street'];
    $house_number = $_POST['house_number'];
    $house_status = $_POST['house_status'];
    $time_address = $_POST['time_address'];
    $employment_status = $_POST['employment_status'];
    $employment_industry = $_POST['employment_industry'];
    $employer_name = $_POST['employer_name'];
    $employer_work_phone = $_POST['employer_work_phone'];
    $month_income = $_POST['month_income'];
    $gender = $_POST['gender'];
    $submit = $_POST['submit'];
    $message = 'Loan Amoutn : ' . $lamount . "\r\n";
    $message .= 'Porpuse Of Loan : ' . $porpuse_of_loan . "\r\n";
    $message .= 'First Name : ' . $fname . "\r\n";
    $message .= 'Last Name : ' . $lname . "\r\n";
    $message .= 'Email Address : ' . $email . "\r\n";
    $message .= 'Phone : ' . $phone . "\r\n";
    $message .= 'Date Of Birth : ' . $date_of_birth . "\r\n";
    $message .= 'Martial Status : ' . $martial_state . "\r\n";
    $message .= 'Number Of Dependants : ' . $number_of_dependants . "\r\n";
    $message .= 'Country : ' . $country . "\r\n";
    $message .= 'city : ' . $city . "\r\n";
    $message .= 'street : ' . $street . "\r\n";
    $message .= 'House Number : ' . $house_number . "\r\n";
    $message .= 'House Status : ' . $house_status . "\r\n";
    $message .= 'Employment Industry : ' . $employment_industry . "\r\n";
    $message .= 'Employer Name : ' . $employer_name . "\r\n";
    $message .= 'Employer Work Phone : ' . $employer_work_phone . "\r\n";
    $message .= 'Monthly Income : ' . $month_income . "\r\n";
    $message .= 'Gender : ' . $gender . "\r\n";

    // reciever mail address
    $to = 'udayraj.mscit@gmail.com';
    $subject = 'Appointment From Loan Plus HTML Template.';
    $headers = 'From: ' . $email . "\r\n" . 'Reply-To: ' . $to . "\r\n";
    if(isset($submit)) {
        if( !empty($email) && !empty($message) ){
            mail($to, $subject, $message, $headers);
            header('Location: appointment-thank.html');
        }
    }
?>