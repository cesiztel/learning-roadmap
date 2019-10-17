C# (pronounced "See Sharp")

- Component-oriented: self-contained and self-describing packages of funcionality.
- Garbage collection automatically reclaims memory occupied by unreachable unused objects.
- Exception handling by error detection and recovery
- Type-safe
- Unified type system: all the types (even the primatives) inherit from a single root object type.

Commands
--------

Create a console application with `--name` or `-n` hello

```
$ donet new console --name hello
```

Types
-----

Some of the types:

## Enums

- Usually it is best to define an enum directly within a namespace so that all classes in the namaespace
can access it with equal convenience. Can be nested within a class or struct.
- First enumarator value starts with 0, and the value of each successibe enumerator is increased by 1.

## Structs

- Typically used to encapsulate small groups of relate variables.
- Contain constructors, constants, fields, methods, properties, indexers, operatos, events and nested types.
Structs can implement an interface but they cannot inherit from another struct. 



