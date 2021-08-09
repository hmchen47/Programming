

<?php
 
if (isset($_POST['firstname']) && isset($_POST['lastname'])) {
    echo $_POST['firstname'].' '.$_POST['lastname'].' uploaded file(s).<br />';
}
 
if (isset($_POST['namesAllFiles']) && $_POST['namesAllFiles'] != "") {
    $folderName = date("m.d.Y");
    if (!is_dir('upload/'.$folderName)) {
        mkdir('upload/'.$folderName);
    }
 
    $filesName = explode("::", $_POST['namesAllFiles']);
    for ($i=0; $i < count($filesName); $i++) {
        copy('upload/RecycleBin/'.$filesName[$i], 'upload/'.$folderName.'/'.$filesName[$i]);
        unlink('upload/RecycleBin/'.$filesName[$i]);
        echo "$filesName[$i] uploaded<br />";
    }
}
 
$fn = (isset($_SERVER['HTTP_X_FILENAME']) ? $_SERVER['HTTP_X_FILENAME'] : false);
 
if ($fn) {
    if (!is_dir('upload/RecycleBin')) {
        mkdir('upload/RecycleBin');
    }
    file_put_contents('upload/RecycleBin/'.$fn, file_get_contents('php://input'));
    exit();
}
 
?>