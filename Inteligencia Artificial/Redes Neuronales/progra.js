var synaptic = require('synaptic');
var jsonfile = require('jsonfile');

var neuronSavedFile = 'neuralNetwork.json';
var variableSavedFile = 'neuralVariables.json';

var neuralNetwork, networkTrainer;

var networkVariables = jsonfile.readFileSync(variableSavedFile);

var Neuron = synaptic.Neuron,
    Layer = synaptic.Layer,
    Network = synaptic.Network,
    Trainer = synaptic.Trainer,
    Architect = synaptic.Architect;

function Perceptron(input, hidden, output)
{
    var inputLayer = new Layer(input);
    var hiddenLayer = new Layer(hidden);
    var outputLayer = new Layer(output);

    inputLayer.project(hiddenLayer);
    hiddenLayer.project(outputLayer);

    this.set({
    	input: inputLayer,
      hidden: [hiddenLayer],
      output: outputLayer
    });

}

Perceptron.prototype = new Network();
Perceptron.prototype.constructor = Perceptron;

function newNetwork(input, output){
   neuralNetwork = new Perceptron(input,networkVariables.hiddenNeurons,output);
}

function loadNetwork(){
   importNetwork(neuronSavedFile);
}

function importNetwork(fileName){
   neuralNetwork = Network.fromJSON(jsonfile.readFileSync(fileName));
}

function trainNetwork(trainerToAssign){
   //Está trabajando con las 16 entradas
   var trainingSet = [
      //Set
   ]

   trainerToAssign.train(trainingSet,{
       rate: networkVariables.alphaRate,
       iterations: networkVariables.iterations,
       error: networkVariables.errorRate
   });

   return trainerToAssign;
}

function exportNetwork(networkToSave, fileName){
   jsonfile.writeFileSync(fileName, networkToSave.toJSON());
}

function askNetwork(networkToAsk, input){
   console.log(networkToAsk.activate(input));
}

function newTrainer(networkToAssign){
   networkTrainer = new Trainer(networkToAssign);
}

function sendDataForAnswer(){
  var insertedArray = document.getElementById('textbox_id').value.split(",");
  if (insertedArray.length !== 16){
    alert("Error. This isn't an array of 16 elements");
  } else {
    //askNetwork(neuralNetwork, insertedArray);
  }
}

//Ejecución
loadNetwork();

//askNetwork(neuralNetwork, [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]);
//askNetwork(neuralNetwork, $(document).getElementById('textbox_id').value.split(","));
