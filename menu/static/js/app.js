rivets.configure({

  // Attribute prefix in templates
  prefix: 'rv',

  // Preload templates with initial data on bind
  preloadData: true,

  // Root sightglass interface for keypaths
  rootInterface: '.',

  // Template delimiters for text bindings
  templateDelimiters: ['{', '}'],

  // Augment the event handler of the on-* binder
  handler: function(target, event, binding) {
    this.call(target, event, binding.view.models)
  }

});

var content = {
    name : "yannick",
    list : [
      { name : "Menu enfant", valide : true},
      { name : "Menu adulte", valide : false},
      { name : "Menu senior", valide : true}
    ]
};

rivets.bind($('#content'), {content: content})