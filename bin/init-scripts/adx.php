#!/usr/bin/php
<?php

$options = array();

$optionPairs = explode(' ', $argv[1]);
foreach ($optionPairs as $optionPair) {
	list($optionKey, $optionValue) = explode('=', $optionPair);
	$optionKey = str_replace('--', '', $optionKey);
	$options[$optionKey] = $optionValue;
}

if (empty($options['prj-name'])) {
	exit('prj-name is not set');
}
if (empty($options['usr-name'])) {
	exit('usr-name is not set');
}

$prjName = $options['prj-name'];
$usrName = $options['usr-name'];

$filePath = __FILE__;
$filePathParts = explode('/', $filePath);
$filePathParts = array_slice($filePathParts, 0, 4);
$path = implode('/', $filePathParts) . '/htdocs/' . $prjName . '/';

$hostTmlPaths[5] = $path . 'host.php.tml';
$hostTmlPaths[4] = $path . 'prj/cfg/host.php.tml';
$hostTmlPaths[3] = $path . 'prj/cfg/host.cfg.ph.tml';

$rulesTable[5] = array(
	"~define\(\s*'ADX_DB_HOST',\s*'.*?'\s*\);~" => "define('ADX_DB_HOST', 'mysql');",
	"~define\(\s*'ADX_DB_USER',\s*'.*?'\s*\);~" => "define('ADX_DB_USER', 'test');",
	"~define\(\s*'ADX_DB_PASSWORD',\s*'.*?'\s*\);~" => "define('ADX_DB_PASSWORD', 'test');",
	"~define\(\s*'ADX_DB_NAME',\s*'.*?'\s*\);~" => "define('ADX_DB_NAME', '{$usrName}_{$prjName}');",
	"~define\(\s*'ADX_URL_HOST',\s*'.*?'\s*\);~" => "define('ADX_URL_HOST', '{$prjName}.{$usrName}');",
	"~define\(\s*'IL_IM_IDENTIFY_PATH',\s*'.*?'\s*\);~" => "define('IL_IM_IDENTIFY_PATH', '/usr/bin/identify');",
	"~define\(\s*'IL_IM_CONVERT_PATH',\s*'.*?'\s*\);~" => "define('IL_IM_CONVERT_PATH', '/usr/bin/convert');",
);

$rulesTable[4] = $rulesTable[5];

$rulesTable[3] = array(
	"~('db'.*?)'nm'\s*=>\s*'.*?'~s" => "$1'nm' => '{$usrName}_{$prjName}'",
	"~('db'.*?)'host'\s*=>\s*'.*?'~s" => "$1'host' => 'mysql'",
	"~('db'.*?)'usr'\s*=>\s*'.*?'~s" => "$1'usr' => 'test'",
	"~('db'.*?)'pwd'\s*=>\s*'.*?'~s" => "$1'pwd' => 'test'",
	"~('http'.*?)'host'\s*=>\s*'.*?'~s" => "$1'host' => '{$prjName}.{$usrName}'",
	"~define\(\s*'IL_IM_IDENTIFY_PATH',\s*'.*?'\s*\);~" => "define('IL_IM_IDENTIFY_PATH', '/usr/bin/identify');",
	"~define\(\s*'IL_IM_CONVERT_PATH',\s*'.*?'\s*\);~" => "define('IL_IM_CONVERT_PATH', '/usr/bin/convert');",
);

$versionNumber = 3;
$maxVersionNumber = 5;
$hostFound = false;

while ($versionNumber <= $maxVersionNumber && !$hostFound) {
	$hostTmlPath = $hostTmlPaths[$versionNumber];
	if (!file_exists($hostTmlPath)) {
		$versionNumber++;
		continue;
	}
	$hostFound = true;

	$hostPath = str_replace('.tml', '', $hostTmlPath);
	copy($hostTmlPath, $hostPath);
	chmod($hostPath, 0777);

	$rules = $rulesTable[$versionNumber];
	$patterns = array_keys($rules);
	$replacements = array_values($rules);

	$hostContent = file_get_contents($hostPath);
	$hostContent = preg_replace($patterns, $replacements, $hostContent);
	file_put_contents($hostPath, $hostContent);
}

if (!$hostFound) {
	echo 'host file is not found';
}