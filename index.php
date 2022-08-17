<?php 
    echo "test<br>";

    $db = mysqli_connect("localhost","root","","myhome");
    if($db){
        echo "sucess<br>";
    }else{
        echo "fail<br>";
    }
    $result =mysqli_query($db,'SELECT VERSION() as VERSION');
    $data = mysqli_fetch_assoc($result);
    echo $data['VERSION'];

?>