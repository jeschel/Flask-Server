<!DOCTYPE html>
<html>
<head>
	<title>LED STATUS</title>
</head>
<body>
	<?php
if($_GET){
    if(isset($_GET['ON'])){
        ON();
    }elseif(isset($_GET['OFF'])){
        OFF();
    }
}

    function ON()
    {
       echo "LED ON.";
    }
    function OFF()
    {
       echo "LED OFF.";
    }

?>
</body>
</html>