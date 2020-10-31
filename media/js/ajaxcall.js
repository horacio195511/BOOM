function reloadList(){
    // delete all of the option in the list
    var list = document.getElementById("model_model");
    while(list.length > 0){
        list.remove(list.length-1);
    }
    var option = document.createElement("option")
    option.text = "--------"
    list.add(option);
    // get the selected company name
    company = document.getElementById('model_company').selectedIndex
    // fetch the list by making ajax call
    var xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var modelList = JSON.parse(xhttp.responseText)
            for(i in modelList){
                var newoption = document.createElement("option")
                newoption.text = modelList[i].name
                list.add(newoption)
            }
        }
    }
    xhttp.open('GET', 'api/modellistupdate?'+'company='+company, true)
    xhttp.send()
}