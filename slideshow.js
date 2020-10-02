//fullscreen the browser


//get the url and stripe it down to just the filename without extention, this gets us the screen-number so this script can be generic.
var myurl=  window.location.href;
myurl = myurl.substring(myurl.lastIndexOf("/") +1)
screennumber=myurl[0]

var images = ""
var slidecount= images.length



var myurl=  window.location.href;
var myurl = myurl.substring(myurl.lastIndexOf("/") +1)
var screennumber=myurl[0]


var data = new XMLHttpRequest();
datalocation = screennumber+"files/filelist.txt"
data.open('GET', datalocation);
data.onreadystatechange = function() {
    //process text file line by line
    slidesdata= data.responseText
    slideimages = slidesdata.split(",")
    slidecount= slideimages.length

}

data.send();
i=0

//document.getElementById("slides").innerHTML = ""
setInterval(function(){ 
  RandomNumber = Math.floor(Math.random() * 100000000)
    console.log(slideimages[i])
    imagelocation= screennumber+ 'files/img/'+slideimages[i]+"?dummy="+RandomNumber
    console.log(imagelocation)
    innerHTMLstring= '<div class="slide" style="background:url('+imagelocation+'); background-size:cover; background-position:center;background-repeat: no-repeat;">' +'</div>'
    document.getElementById("slides").innerHTML = innerHTMLstring
    if (i < slidecount){ i++}
    if (i >= slidecount){i=0}
        }, 10000);
