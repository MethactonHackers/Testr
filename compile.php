<?php if (isset($_POST[ "json"])) { $json=$_POST[ "json"]; $json=addslashes($json); }else echo "{'success': false, 'details': 'y u dumb'}"; ?>
