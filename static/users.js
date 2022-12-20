let form = document.getElementById('add-form')
let form_cover = document.querySelector('#add-form .add-form-cover')
let currentAdvert = null


form_cover.addEventListener('click', event => {
	form.style.display = 'none'
	form.style.opacity = 0

	form.querySelectorAll('.add-form-user-roles small').forEach(item => item.remove())
})

function userCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}/users/update/${card.querySelector('.user-id').innerText}`
	)

	form.querySelector('#name').value = card.querySelector('.user-first-name').innerText
	form.querySelector('#role').value = card.querySelector('.user-role').innerText
}


function feeCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1
	form.querySelector('.add-category-form').setAttribute('action', `${window.location.origin}/fees/update`)

	form.querySelector('#price').value = card.querySelector('.fee-price').innerText
	form.querySelector('#payment').value = card.querySelector('.fee-payment').innerText
	form.querySelector('#distance').value = card.querySelector('.fee-distance').innerText
	form.querySelector('#nonpaid').value = card.querySelector('.fee-nonpaid').innerText
}

function advertCard(data){
	form.style.display = 'flex'
	form.style.opacity = 1

	data = JSON.parse(data)
	currentAdvert = data

	form.querySelector('.advert-id').innerText = data.id
	form.querySelector('.advert-title-uz').innerText = data.title.uz
	form.querySelector('.advert-title-ru').innerText = data.title.ru
	form.querySelector('.advert-title-en').innerText = data.title.en
	form.querySelector('.advert-content-ru').innerText = data.content.ru
	form.querySelector('.advert-view-image').setAttribute('src', data.imageUrl)

	form.querySelector('.advert-form-button-edit').setAttribute('data-id', data.id)
	form.querySelector('.advert-form-button-remove').setAttribute('data-id', data.id)
}

function removeAdvert(button){
	if (confirm('Вы действительно хотите удалить?')) {
		window.location.replace(window.location.origin + '/adverts/delete/' + button.getAttribute('data-id'))
	}
}

function editAdvert(button){
	form.style.display = 'none'
	form.style.opacity = 0

	panel = document.getElementById('advert-add')
	panel.style.display = 'flex'
	panel.style.opacity = 1

	panel.querySelector('.advert-form-add').setAttribute('action', '/adverts/update/' + button.getAttribute('data-id'))

	panel.querySelector('input[name="title_uz"]').value = currentAdvert.title.uz
	panel.querySelector('input[name="title_ru"]').value = currentAdvert.title.ru
	panel.querySelector('input[name="title_en"]').value = currentAdvert.title.en

	panel.querySelector('textarea[name="content_ru"]').value = currentAdvert.content.ru
	panel.querySelector('textarea[name="content_uz"]').value = currentAdvert.content.uz
	panel.querySelector('textarea[name="content_en"]').value = currentAdvert.content.en
	
	panel.querySelector('input[type="file"]').removeAttribute('required')

	panel.querySelector('.add-form-cover').addEventListener('click', event => {
		panel.style.display = 'none'
		panel.style.opacity = 0
	})
}

try{
	let panel = document.getElementById('advert-add')
	call_button.addEventListener('click', event => {
		panel.style.display = 'flex'
		panel.style.opacity = 1

		panel.querySelector('.advert-form-add').setAttribute('action', call_button.getAttribute('data-link'))

		panel.querySelector('input[name="title_uz"]').value = ""
		panel.querySelector('input[name="title_ru"]').value = ""
		panel.querySelector('input[name="title_en"]').value = ""

		panel.querySelector('textarea[name="content_ru"]').value = ""
		panel.querySelector('textarea[name="content_uz"]').value = ""
		panel.querySelector('textarea[name="content_en"]').value = ""

		panel.querySelector('input[type="file"]').setAttribute('required', 'true')

		panel.querySelector('.add-form-cover').addEventListener('click', event => {
			panel.style.display = 'none'
			panel.style.opacity = 0
		})
	})
} catch(error){}