
function renderiza_total_gasto(url){
    fetch(url, {
        method: 'get',
    }).then(funcition(result){
        return result.json()
    }).then(funcition(data){
        document.getElementById('total_gasto').innerHTML = data.total
    })
}