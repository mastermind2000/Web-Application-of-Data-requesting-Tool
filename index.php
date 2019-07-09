<!DOCTYPE html>
<link rel = "stylesheet" type="text/css" href="middle.css">
<html>
<br>
<br>
<br>
<body style = "color:white">
<h3 align="center">Enter Pret And Post Time to proceed</h3>
<div id = "form-wrapper">
<form action=FetchData.php?Pre='.$Pre.'&Pos='.$Pos.' method="get" target="_blank">
  Pre time: <input type="number", name="Pre" class="click" required/><br> <br>
  Pos time: <input type="number", name="Pos" class="click" required/><br>
  <button name="Submit" class="click">Submit</button>
</form>
</div>
</br>
</br>
</br>
<br>
<br>
<br>
<br>
<br>
<br>
</body>
<?php

  if(isset($_GET['Submit']))
  {
    $Pre=$_GET['Pre'];
    $Pos=$_GET['Pos'];
    echo $Pre;
    echo $Pos;
  }

?>
<?php include 'decorate.html' ?>
</html>
