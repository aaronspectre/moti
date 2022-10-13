let panel = document.getElementById('add-form')
let cover = document.querySelector('.add-form-cover')
let form = document.querySelector('add-product-form')
let canvas = document.getElementById('qr')


cover.addEventListener('click', event => {
	panel.style.display = 'none'
	panel.style.opacity = 0
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
	document.getElementById('order-view-address').innerText = order.address
	document.getElementById('order-view-comment').innerText = order.comments
	document.getElementById('order-view-order').innerText = products.join('\n')
	document.getElementById('order-view-type').innerText = order.orderType
	document.getElementById('order-view-pay').innerText = order.payType

	document.getElementById('order-cancel-button').setAttribute('href', `${window.origin}/update/${order.id}/CANCELLED`)
	document.getElementById('order-deliver-button').setAttribute('href', `${window.origin}/update/${order.id}/DELIVER`)

	qrcode = new QRious({
		element: canvas,
		background: 'white',
		foreground: '#292929',
		level: 'H',
		size: 182,
		value: String(order.id)
	})
}