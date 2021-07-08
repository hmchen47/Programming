<?php
if (isset($_POST['firstname']) && isset($_POST['lastname'])) {
	echo $_POST['firstname'] . ' ' . $_POST['lastname'] . ' try to upload file(s).';
}

if (isset($_FILES) && is_array($_FILES)) {
	$number_files_send = count($_FILES['formFiles']['name']);
	$dir = realpath('.') . '/upload/';

	if ($number_files_send > 0) {
		for ($i = 0; $i < $number_files_send; $i++) {
			echo '<br/>Reception of : ' . $_FILES['formFiles']['name'][$i];
			$copy = move_uploaded_file($_FILES['formFiles']['tmp_name'][$i], $dir . $_FILES['formFiles']['name'][$i]);
			if ($copy) {
				echo '<br />File ' . $_FILES['formFiles']['name'][$i] . ' copy';
			}
			else {
				echo '<br />No receive file';
			}
		}
	}
}   

?>