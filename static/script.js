let form = document.getElementById('add-form')
let form_cover = document.querySelector('#add-form .add-form-cover')
let call_form_button = document.getElementById('call-form-button')
let products = Array()

call_form_button.addEventListener('click', event => {
	form.style.display = 'flex';
	form.style.opacity = 1

	form.querySelector('form').setAttribute('action', call_form_button.getAttribute('data-link'))

	input = form.querySelector('form')
	input.querySelector("[name = 'name_uz']").value = ''
	input.querySelector("[name = 'name_ru']").value = ''
	input.querySelector("[name = 'name_en']").value = ''
})

form_cover.addEventListener('click', event => {
	form.style.display = 'none';
	form.style.opacity = 0
})


function editCategory(card, link){
	card = card.parentNode.parentNode

	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = card.querySelector('.card-name-uz').innerText
	input.querySelector("[name = 'name_ru']").value = card.querySelector('.card-name-ru').innerText
	input.querySelector("[name = 'name_en']").value = card.querySelector('.card-name-en').innerText
}

function editProduct(card, link, id){
	product = products[id - 1]
	form.style.display = 'flex';
	form.style.opacity = 1

	input = form.querySelector('form')
	input.setAttribute('action', link)

	input.querySelector("[name = 'name_uz']").value = product['productName']['uz']['text']
	input.querySelector("[name = 'name_ru']").value = product['productName']['ru']['text']
	input.querySelector("[name = 'name_en']").value = product['productName']['eng']['text']

	input.querySelector("[name = 'desc_uz']").value = product['description']['uz']['text']
	input.querySelector("[name = 'desc_ru']").value = product['description']['ru']['text']
	input.querySelector("[name = 'desc_en']").value = product['description']['eng']['text']

	input.querySelector("[name = 'discount']").value = product['discount']
	input.querySelector("[name = 'price']").value = product['price']
	input.querySelector("[name = 'time']").value = Number(product['readyTime'].replace('min', ''))

	// input.querySelector("[name = 'category']").value = product['categoryId']
}