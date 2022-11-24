function renderiza_total_gasto(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_gasto').innerHTML = data.total
    })

}