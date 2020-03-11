function stringToHex(str) {
    var val = "";
    for (var i = 0; i < str.length; i++) {
        if (val == "") val = str.charCodeAt(i).toString(16); else val += str.charCodeAt(i).toString(16);
    }
    return val;
}

var width = 1400;
var height = 900;
var screendate = width + "," + height;
cookie_data = "srcurl=" + stringToHex("http://www.300600900.cn/");
security_verify_data = "/?security_verify_data=" + stringToHex(screendate);

