<h1 align="center">
  <br>
  <a href="https://www.rna.org.co/"><img src="https://images.unsplash.com/photo-1643780668909-580822430155?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2064&q=80" alt="WHR" width="400"></a>
  <br>
  RNA Taxonomy Classification
  <br>
</h1>

<h4 align="center">A Random Forest Multiclass classifier built in scikit-learn using Markov Chains. 
</h4>

<p align="center">
  <a href='https://github.com/shivamkapasia0' target="_blank"><img alt='scikit-learn' src='https://img.shields.io/badge/scikit-learn-100000?style=for-the-badge&logo=scikit-learn&logoColor=FFFFFF&labelColor=FF6A00&color=1882EA'/></a> <a href='https://numpy.org/' target="_blank"><img alt='Numpy' src='https://img.shields.io/badge/Numpy-100000?style=for-the-badge&logo=Numpy&logoColor=4C16ED&labelColor=60A7FD&color=3566ED'/></a> <a href='https://joblib.readthedocs.io/en/latest/' target="_blank"><img alt='joblib' src='https://img.shields.io/badge/Joblib-100000?style=for-the-badge&logo=joblib&logoColor=EA1616&labelColor=BD9B7A&color=000000'/></a> <a href='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0tfXl3Iv7AhUVTDABHZOWB-AQFnoECBEQAQ&url=https%3A%2F%2Fwww.json.org%2F&usg=AOvVaw3WUMhwoap01T91PbRZTt_w' target="_blank"><img alt='json' src='https://img.shields.io/badge/Json-100000?style=for-the-badge&logo=json&logoColor=3C3B3B&labelColor=D7CEC7&color=D7D7D7'/></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> 
</p>

![screenshot](https://upload.wikimedia.org/wikipedia/commons/5/57/ARNm-Rasmol.gif)

## Key Features

* This machine learning model takes a RNA sequence and predicts what class does it belong to. Classes are taken as taxonomies. The avaible taxonomies are the following 19:

  - Orthomyxoviridae
  - Rhabdoviridae
  - Arteriviridae
  - Coronaviridae
  - Reoviridae
  - Caliciviridae
  - Phenuiviridae
  - Hantaviridae
  - Picornaviridae
  - Betaflexiviridae
  - Astroviridae
  - Closteroviridae
  - Flaviviridae
  - Potyviridae
  - Retroviridae
  - Togaviridae
  - Paramyxoviridae
  - Hepeviridae
  - Pneumoviridae

* Before Prediction the model computes a markov chain whose states are the 64 writeable codons with the nucleoids **A, C, G, T** and then computes metrics over its adjacent associated matrix: 8 of them are matricial norms and the missing 10 parameters are the first eigenvalues complex norms ascending ordered. Namely:
  - `Frobenius Norm`
  - `Nuclear Norm`
  - `Infty Norm`
  - `Neg Infty Norm`
  - `Neg L1 Norm`
  - `L1 Norm`
  - `Neg L2 Norm` 
  - `L2 Norm`
  - `eig 1` 
  - `eig 2` 
  - `eig 3` 
  - `eig 4` 
  - `eig 5` 
  - `eig 6` 
  - `eig 7` 
  - `eig 8` 
  - `eig 9` 
  - `eig 10` 
  
 With this new metrics, we built a new dataset. and we found this scatter plot:
 ![screenshot](https://github.com/santiagoahl/rna-taxonomy-prediction/blob/main/results/scatter.png)

 

* We implemented a **Random Forest model** whose train data is taken from the new dataset.
![screenshot](https://1.bp.blogspot.com/-Ax59WK4DE8w/YK6o9bt_9jI/AAAAAAAAEQA/9KbBf9cdL6kOFkJnU39aUn4m8ydThPenwCLcBGAsYHQ/s0/Random%2BForest%2B03.gif)
* We archieved a **97.1%** of val score.
* The confusion matrix is the following

![screenshot](https://github.com/santiagoahl/RNA-taxonomy-prediction/blob/main/results/confusion_matrix.png)
* The learning curve is the following
![screenshot](https://github.com/santiagoahl/rna-taxonomy-prediction/blob/main/results/learning_curves.png)


## How To Use

To clone and run this application, follow these steps

```bash
# Clone this repository
$ git clone https://github.com/santiagoahl/rna-taxonomy-prediction.git

# Go into the repository
$ cd rna-taxonomy-prediction

# Go to jupyter notebooks
$ jupyter-notebook

# Run the Libraries & Modules cell
# Run the Model Import cell
```

## Credits

This software uses the following packages:

- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Numpy](https://numpy.org/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)


## License

MIT

---

> Web Site [santiagoal.super.site](https://santiagoal.super.site/) &nbsp;&middot;&nbsp;
> GitHub [@santiagoahl](https://github.com/santiagoahl) &nbsp;&middot;&nbsp;
> Twitter [@sahumadaloz](https://twitter.com/sahumadaloz)
