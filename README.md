# Swetest

This is a simple Python wrapper for the high precision swisseph application swetest. Swetest computes a complete set of geocentric planetary positions, for a given date or a sequence of dates. It can be used from the commandline, or loaded from a class. 

## Installation

The project can be installed using pip:

```
pip install swetest
```

Or when you want to use the setuup command to install the project and its dependencies, run:

```
pip install -r requirements.txt
python setup.py install
```

## Usage

The project can be used for both from the commandline and loaded from a class.

When used on the command line simply do:

```
python -m swetest --query="-p1 -d0 -b1.12.1900 -n10 -fPTl -head"
```

When loading the class in your project, first import module:

```
    from swetest import Swetest
```

Then you can directly query and execute swetest load the class and execute the query:

```
    swetest = Swetest()
    swetest.query('-p1 -d0 -b1.12.1900 -n10 -fPTl -head')->execute();
    print(swetest.get_output())

    Another option is to pass a list object(note: do not add - to the flags"):

        the_query = [
            'p1',
            'd0',
            'b1.12.1900',
            'n10',
            'fPTl',
            'head'
        ]

        swetest.query(the_query)->execute();
        print(swetest.get_output())
```

Which in both cases result in:

```
    Returns:
    -------
    Moo-Sun 01.12.1900  106.6451392
    Moo-Sun 02.12.1900  120.0074533
    Moo-Sun 03.12.1900  133.5161823
    Moo-Sun 04.12.1900  147.0977240
    Moo-Sun 05.12.1900  160.6609399
    Moo-Sun 06.12.1900  174.1058642
    Moo-Sun 07.12.1900 -172.6643512
    Moo-Sun 08.12.1900 -159.7310200
    Moo-Sun 09.12.1900 -147.1500247
    Moo-Sun 10.12.1900 -134.9464751
```