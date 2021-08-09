<?php

if (isset($_POST['firstname']) && isset($_POST['lastname'])) {
	echo $_POST['firstname'] . ' ' . $_POST['lastname'] . ' try to upload file(s).';
}

$folderName = date("m.d.Y");
if (!is_dir('upload/'.$folderName)) {
	mkdir('upload/'.$folderName);
}

$fn = (isset($_SERVER['HTTP_X_FILENAME']) ? $_SERVER['HTTP_X_FILENAME'] : false);
if ($fn)
{
	file_put_contents('upload/' . $folderName . '/' . $fn, file_get_contents('php://input'));
	echo "$fn uploaded";
	exit();
}
else {
	if (isset($_FILES) && is_array($_FILES) && array_key_exists('formFiles', $_FILES)) {
		$number_files_send = count($_FILES['formFiles']['name']);
		$dir = realpath('.') . '/upload/' . $folderName . '/';
		
		if ($number_files_send > 0) {
			for ($i = 0; $i < $number_files_send; $i++) {
				echo '<br/>Reception of : ' . $_FILES['formFiles']['name'][$i];
				$copy = move_uploaded_file($_FILES['formFiles']['tmp_name'][$i], $dir . $_FILES['formFiles']['name'][$i]);
				if ($copy) {
					echo '<br />File ' . $_FILES['formFiles']['name'][$i] . ' copy';
				}
				else {
					echo '<br />No file to upload';
				}
			}
		}
	}   
}

?>