let panel = document.getElementById('add-form')
let covers = document.querySelectorAll('.add-form-cover')
let form = document.querySelector('add-product-form')


covers.forEach(cover => {
	cover.addEventListener('click', event => {
		panel.style.display = 'none'
		panel.style.opacity = 0
	})
})


function showOrder(order) {
	panel.style.display = 'flex'
	panel.style.opacity = 1

	products = Array()
	for (var i = order.products.length - 1; i >= 0; i--) {
		products.push(`x${order.products[i].count} ${order.products[i].productName}`)
	}


	dateOptions = {day: 'numeric', month: 'short', hour: 'numeric', minute: 'numeric', hour12: false}

	document.getElementById('order-view-phone').innerText = order.user
	document.getElementById('order-view-price').innerText = order.price
	document.getElementById('order-view-status').innerText = order.status
	document.getElementById('order-view-date').innerText = new Date(order.creationTime).toLocaleDateString('en-US', dateOptions)
	document.getElementById('order-view-phone').innerText = order.user
	document.getElementById('order-view-delivery').innerText = order.deliveryTime
	document.getElementById('order-view-address').innerText = order.addressRes
	document.getElementById('order-view-comment').innerText = order.comments
	document.getElementById('order-view-order').innerText = products.join('\n')
	document.getElementById('order-view-type').innerText = order.orderType
	document.getElementById('order-view-pay').innerText = order.paymentMethod

	document.getElementById('status-changer').value = order.status
	document.getElementById('status-changer').setAttribute('data-id', order.id)
}

function changeStatus(option) {
	let orderId = option.getAttribute('data-id')
	let url = `${window.origin}/update/${orderId}/${option.value}`
	response = fetch(url).then(response => (response.status == 200) ? location.reload() : null)
}