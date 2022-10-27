let form = document.getElementById('add-form')
let call_button = document.getElementById('call-form-button')
let form_cover = document.querySelector('#add-form .add-form-cover')


form_cover.addEventListener('click', event => {
	form.style.display = 'none'
	form.style.opacity = 0
})


call_button.addEventListener('click', event => {
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}${call_button.getAttribute('data-link')}`
	)

	form.querySelector('#price').value = ''
	form.querySelector('#payment').value = ''
})


function userCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('#name').value = card.querySelector('.user-first-name').innerText
	form.querySelector('#phone').value = card.querySelector('.user-phone-number').innerText
	form.querySelector('#role').value = card.querySelector('.user-role').innerText
	console.log(card.querySelector('.user-role').innerText)
}


function feeCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1
	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}/fees/update/${card.querySelector('.fee-id').innerText}`
	)

	form.querySelector('#price').value = card.querySelector('.fee-price').innerText
	form.querySelector('#payment').value = card.querySelector('.fee-payment').innerText
}