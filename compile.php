<?php if (isset($_POST[ "json"])) { $json=$_POST[ "json"]; file_put_contents( "CurrentJSON.json", $json); $command_output=`python make_tex.py 2>&1`; $milliseconds=round(microtime(true) * 1000); $file=hash( "sha256", "$milliseconds"); copy( "CurrTEX.pdf", "temp/".$file); /*unlink( "CurrTEX.pdf"); */echo "{'success': true, 'location': 'temp/$file', 'details': 'yay'}";}else echo "{'success': false, 'details': 'y u dumb'}"; ?>
