
// Based on https://gcc.gnu.org/wiki/Visibility
#if defined _WIN32 || defined __CYGWIN__
    #ifdef __GNUC__
        #define DLL_EXPORT __attribute__ ((dllexport))
    #else
        #define DLL_EXPORT __declspec(dllexport)
    #endif
#else
    #define DLL_EXPORT __attribute__ ((visibility ("default")))
#endif

#include <dolfin/function/Expression.h>
#include <dolfin/math/basic.h>
#include <Eigen/Dense>


// cmath functions
using std::cos;
using std::sin;
using std::tan;
using std::acos;
using std::asin;
using std::atan;
using std::atan2;
using std::cosh;
using std::sinh;
using std::tanh;
using std::exp;
using std::frexp;
using std::ldexp;
using std::log;
using std::log10;
using std::modf;
using std::pow;
using std::sqrt;
using std::ceil;
using std::fabs;
using std::floor;
using std::fmod;
using std::max;
using std::min;

const double pi = DOLFIN_PI;


namespace dolfin
{
  class dolfin_expression_d95439b66d1ce1cb1562be3931ea14f0 : public Expression
  {
     public:
       double t;


       dolfin_expression_d95439b66d1ce1cb1562be3931ea14f0()
       {
            
       }

       void eval(Eigen::Ref<Eigen::VectorXd> values, Eigen::Ref<const Eigen::VectorXd> x) const override
       {
          values[0] = // Not supported in C:
// ImmutableDenseNDimArray
[1.27672191597265e+24, 1.2767219115924e+24, 1.27672196228817e+24, 1.27672191597265e+24, 1.27672203513207e+24, 1.27672196228817e+24, 1.27672213638581e+24, 1.27672203513206e+24, 1.27672226631401e+24, 1.27672213638581e+24, 1.2767224249958e+24, 1.27672226631401e+24, 1.27672261246334e+24, 1.2767224249958e+24, 1.27672282873221e+24, 1.27672261246334e+24, 1.2767230738109e+24, 1.27672282873221e+24, 1.2767233477044e+24, 1.2767230738109e+24, 1.2767236504159e+24, 1.27672334770441e+24, 1.27672398194746e+24, 1.27672365041589e+24, 1.27672434230053e+24, 1.27672398194746e+24, 1.27672473147612e+24, 1.27672434230053e+24, 1.27672514947499e+24, 1.27672473147612e+24, 1.27672559629768e+24, 1.27672514947498e+24, 1.27672607194462e+24, 1.27672559629768e+24, 1.27672657641614e+24, 1.27672607194462e+24, 1.2767271097125e+24, 1.27672657641614e+24, 1.2767276718339e+24, 1.2767271097125e+24, 1.27672826278052e+24, 1.2767276718339e+24, 1.27672888255249e+24, 1.27672826278052e+24, 1.27672953114992e+24, 1.27672888255249e+24, 1.2767302085729e+24, 1.27672953114992e+24, 1.27673091482152e+24, 1.2767302085729e+24, 1.27673164989584e+24, 1.27673091482152e+24, 1.27673241379592e+24, 1.27673164989584e+24, 1.2767332065218e+24, 1.27673241379592e+24, 1.27673402807353e+24, 1.2767332065218e+24, 1.27673487845115e+24, 1.27673402807353e+24, 1.27673575765468e+24, 1.27673487845114e+24, 1.27673666568415e+24, 1.27673575765467e+24, 1.27673760253959e+24, 1.27673666568415e+24, 1.27673856822101e+24, 1.27673760253958e+24, 1.27673956272845e+24, 1.27673856822101e+24, 1.2767405860619e+24, 1.27673956272844e+24, 1.2767416382214e+24, 1.2767405860619e+24, 1.27674271920695e+24, 1.2767416382214e+24, 1.27674382901856e+24, 1.27674271920695e+24, 1.27674496765624e+24, 1.27674382901856e+24, 1.27674613512001e+24, 1.27674496765624e+24, 1.27674733140988e+24, 1.27674613512001e+24, 1.27674855652584e+24, 1.27674733140988e+24, 1.27674981046791e+24, 1.27674855652584e+24, 1.2767510932361e+24, 1.27674981046791e+24, 1.27675240483041e+24, 1.2767510932361e+24, 1.27675374525085e+24, 1.27675240483041e+24, 1.27675511449742e+24, 1.27675374525085e+24, 1.27675651257012e+24, 1.27675511449741e+24, 1.27675793946896e+24, 1.27675651257012e+24, 1.27675939519395e+24, 1.27675793946896e+24, 1.27676087974509e+24, 1.27675939519395e+24, 1.27676239312237e+24, 1.27676087974509e+24, 1.27676393532582e+24, 1.27676239312237e+24, 1.27676550635542e+24, 1.27676393532582e+24, 1.27676710621118e+24, 1.27676550635542e+24, 1.2767687348931e+24, 1.27676710621118e+24, 1.27677039240118e+24, 1.2767687348931e+24, 1.27677207873544e+24, 1.27677039240118e+24, 1.27677379389586e+24, 1.27677207873544e+24, 1.27677553788245e+24, 1.27677379389586e+24, 1.27677731069522e+24, 1.27677553788245e+24, 1.27677911233416e+24, 1.27677731069522e+24, 1.27678094279928e+24, 1.27677911233416e+24, 1.27678280209057e+24, 1.27678094279928e+24, 1.27678469020804e+24, 1.27678280209057e+24, 1.27678660715169e+24, 1.27678469020804e+24, 1.27678855292153e+24, 1.27678660715169e+24, 1.27679052751754e+24, 1.27678855292153e+24, 1.27679253093974e+24, 1.27679052751754e+24, 1.27679456318812e+24, 1.27679253093974e+24, 1.27679662426269e+24, 1.27679456318812e+24, 1.27679871416344e+24, 1.27679662426269e+24, 1.27680083289039e+24, 1.27679871416344e+24, 1.27680298044351e+24, 1.27680083289039e+24, 1.27680515682283e+24, 1.27680298044351e+24, 1.27680736202834e+24, 1.27680515682283e+24, 1.27680959606003e+24, 1.27680736202834e+24, 1.27681185891792e+24, 1.27680959606003e+24, 1.276814150602e+24, 1.27681185891792e+24, 1.27681647111227e+24, 1.276814150602e+24, 1.27681882044873e+24, 1.27681647111227e+24, 1.27682119861139e+24, 1.27681882044873e+24, 1.27682360560024e+24, 1.27682119861139e+24, 1.27682604141528e+24, 1.27682360560024e+24, 1.27682850605652e+24, 1.27682604141528e+24, 1.27683099952395e+24, 1.27682850605652e+24, 1.27683352181758e+24, 1.27683099952395e+24, 1.2768360729374e+24, 1.27683352181758e+24, 1.27683865288342e+24, 1.2768360729374e+24, 1.27684126165563e+24, 1.27683865288342e+24, 1.27684389925404e+24, 1.27684126165563e+24, 1.27684656567865e+24, 1.27684389925404e+24, 1.27684926092946e+24, 1.27684656567865e+24, 1.27685198500646e+24, 1.27684926092946e+24, 1.27685473790966e+24, 1.27685198500646e+24, 1.27685751963906e+24, 1.27685473790966e+24, 1.27686033019466e+24, 1.27685751963906e+24, 1.27686316957646e+24];

       }

       void set_property(std::string name, double _value) override
       {
          if (name == "t") { t = _value; return; }
       throw std::runtime_error("No such property");
       }

       double get_property(std::string name) const override
       {
          if (name == "t") return t;
       throw std::runtime_error("No such property");
       return 0.0;
       }

       void set_generic_function(std::string name, std::shared_ptr<dolfin::GenericFunction> _value) override
       {

       throw std::runtime_error("No such property");
       }

       std::shared_ptr<dolfin::GenericFunction> get_generic_function(std::string name) const override
       {

       throw std::runtime_error("No such property");
       }

  };
}

extern "C" DLL_EXPORT dolfin::Expression * create_dolfin_expression_d95439b66d1ce1cb1562be3931ea14f0()
{
  return new dolfin::dolfin_expression_d95439b66d1ce1cb1562be3931ea14f0;
}

