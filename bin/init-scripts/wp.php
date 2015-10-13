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

$fromPath = $path . 'wp-config-sample.php';
$toPath = $path . 'wp-config.php';

copy($fromPath, $toPath);
chmod($toPath, 0777);

$rules = array(
	"~define\(\s*'DB_HOST',\s*'.*?'\s*\);~" => "define('DB_HOST', 'mysql');",
	"~define\(\s*'DB_USER',\s*'.*?'\s*\);~" => "define('DB_USER', 'test');",
	"~define\(\s*'DB_PASSWORD',\s*'.*?'\s*\);~" => "define('DB_PASSWORD', 'test');",
	"~define\(\s*'DB_NAME',\s*'.*?'\s*\);~" => "define('DB_NAME', '{$usrName}_{$prjName}');",
);

$patterns = array_keys($rules);
$replacements = array_values($rules);

$content = file_get_contents($toPath);
$content = preg_replace($patterns, $replacements, $content);
file_put_contents($toPath, $content);
