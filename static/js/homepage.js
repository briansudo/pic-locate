function register_sign_in_modal(action) {
  console.log('went here');
  if (action == 'register') {
    $.ajax({
      url : "static/modal-html/register-modal.html",
      success : function(result){
        $("#register-sign-in-modal-header").html('Register');
        $("#register-sign-in-modal-body").html(result);
        $("#register-sign-in-modal").modal('show');
      }
    });
  } else {
    $.ajax({
      url : "static/modal-html/sign-in-modal.html",
      success : function(result){
        $("#register-sign-in-modal-header").html('Sign in');
        $("#register-sign-in-modal-body").html(result);
        $("#register-sign-in-modal").modal('show');
      }
    });
  }
}
