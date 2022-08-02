<?php

$student = array("王小明","陳美麗","羅玉兔","蔡小英");

echo $student[0] . "<br>";
echo $student[3];
echo "<br>";

echo "<hr>"; //分隔線

$i = count($student); //陣列中的數量

for ($x=0 ; $x<$i; $x++){
	echo $student[$x] . "<br>";
	
}

echo "<hr>"; 

/*foreach 是php用來輸出陣列方式使用的
使用上來比較快且直覺
foreach(陣列名稱 as $變數){
	echo $變數
} */

foreach($student as $value){
	echo $value."<br>";
}


?>