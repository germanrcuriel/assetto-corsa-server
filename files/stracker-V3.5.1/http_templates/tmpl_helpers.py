# -*- coding: utf-8 -*-

# Copyright 2015-2016 NEYS
# This file is part of sptracker.
#
#    sptracker is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    sptracker is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


from bottle import SimpleTemplate

class MyTemplate(SimpleTemplate):
    def __init__(self, t, **kw):
        self.kw = kw
        SimpleTemplate.__init__(self,t)

    def render(self, **kw):
        kw.update(self.kw)
        return SimpleTemplate.render(self, kw)

car_info = {}

def set_car_info(new_car_info):
    for c in new_car_info:
        car_info[c] = new_car_info[c]

car_tmpl = MyTemplate("""\
% from stracker_lib.logger import *
% try:
%    tooltip
% except:
%    tooltip = False
% end
% try:
%    if uicar in [None, car]:
%        raise RuntimeError
%    end
% except:
%    uicar = car_info.get(car, {}).get('uiname', car)
% end
%
% def longestSubString(s1, s2):
%   i = 0
%   while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
%     i+=1
%   end
%   return s1[:i]
% end
%
% def unbrand(car, uicar):
%     if uicar is None:
%         return car
%     end
%     if car in car_info:
%         brand = car_info[car].get('brand','')
%         if not brand is None:
%             ls = longestSubString(uicar.lower(), brand.lower())
%         else:
%             ls = ""
%         end
%         if len(ls) < 3:
%             ls = ""
%         end
%         uicar = uicar[len(ls):].strip()
%     else:
%         pass
%     end
%     return uicar
% end
%
% def carbadge(car):
%     return car_info.get(car, {}).get('brand','')
% end
%
% needsText=True
% brand = carbadge(car)
% if brand:
<img src="carbadge?car={{!car}}"
%     if tooltip:
%           needsText=False
            title="{{uicar}}"
%     else:
            title="{{brand}}"
%     end
            class="aids">
% end
% if needsText:
    {{unbrand(car,uicar)}}
% end
% if carbadge(car):
</img>
% end
""", **{'car_info':car_info})