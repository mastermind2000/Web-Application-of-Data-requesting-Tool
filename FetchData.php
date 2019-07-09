<!DOCTYPE html>
<html>
<body style = "color:white">
<link rel = "stylesheet" type="text/css" href="decoFetchpage.css">
<div id = "form-wrapper">
<form action="" method="post" enctype="multipart/form-data">
 catalog file:<input type = "file" name= "File1" id = "fileToUpload1" required/>
 stationfile:<input type = "file" name= "File2" id = "fileToUpload2" required/>
 <button name="Fetch" class="click">Fetch</button>
</form>
</div>

<?php
        $Pre=$_GET['Pre'];
        $Pos=$_GET['Pos'];	
 	if(isset($_POST['Fetch']))
  	{
    		#$Pre=5;
    		#$Pos=100;
    		$target_dir = "Input/";
		$target_file1 = $target_dir.$_FILES["File1"]["name"];
		$target_file2 = $target_dir.$_FILES["File2"]["name"];
	
	        $uploadOk = 1;
		move_uploaded_file($_FILES["File1"]["tmp_name"], $target_file1);
		move_uploaded_file($_FILES["File2"]["tmp_name"], $target_file2);

		$filename = $_FILES["File1"]["name"];
		$cmd='/var/www/html/FetchData.sh '.$Pre.' '.$Pos.' 1>/dev/null 2>/dev/null';
	    	system($cmd);
	    	echo '<a href="Output/Data.zip">Download file</a>';
  	}
?>
<img src="circle.jpg">
</link>
</html>
