function init_profile_invite()
{	
	var container = $('#js_invite');
	var log = container.find("#js_invite_log");
	var invites_count_el = container.find("#invites_count");
	var form = $('#js_invite form'); 
	
	function add_message(is_error, msg) {
		li = $("<li>" + msg + "</li>");
		if (is_error) {
			$(msg).addClass("error");
		} else {
			inv_count = parseInt(invites_count_el.text());
			inv_count--;
			invites_count_el.text(inv_count);
			if (inv_count <= 0) {
				form.hide();
			}
			form.find("#id_email").val("");
		}
		log.append(li);
	}
	
	function on_response(data) {
		try {
			response = eval("(" + data + ")");
		} catch(err) {
			msg = "error: response parse exception"
			
		}
		if (response.error) {
			add_message(true, response.error);
		} else {
			add_message(false, "Sended to " + response.email);
		}
	}
	
	form.submit( function() {
		$.post('/invite', {'email': $(this).find('#id_email').val()}, on_response);
		return false;
	})	
}

$(document).ready(function(){
	init_profile_invite();
})